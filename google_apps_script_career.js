/*
 * Google Apps Script — Career Form Handler
 * 
 * INSTRUCTIONS:
 * 1. Open your Google Sheet for Careers
 * 2. Go to Extensions → Apps Script
 * 3. Delete all existing code and paste this entire file
 * 4. Save, then Deploy → New deployment → Web app
 *    - Execute as: Me
 *    - Who has access: Anyone
 * 5. Copy the deployed URL and provide it back here!
 */

function doPost(e) {
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    // Handle both FormData (e.parameter) and JSON (e.postData.contents)
    var data;
    if (e.parameter && e.parameter.name) {
      data = e.parameter;
    } else {
      data = JSON.parse(e.postData.contents);
    }
    
    // Format timestamp in Indian Standard Time (IST / GMT+05:30)
    var formattedTimestamp = Utilities.formatDate(new Date(), "GMT+05:30", "dd/MM/yyyy HH:mm:ss");
    
    // Append a new row with the form data
    sheet.appendRow([
      data.name,           // A: Name
      data.email,          // B: Email
      data.phone,          // C: Contact Number
      data.training_code,  // D: Training Code
      data.brief,          // E: Brief
      data.source || '',   // F: Source Link (which WhatsApp link they came from)
      formattedTimestamp    // G: Timestamp
    ]);
    
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'success', message: 'Data saved successfully' }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

// Handle GET requests (for testing the deployment)
function doGet(e) {
  return ContentService
    .createTextOutput(JSON.stringify({ status: 'ok', message: 'SAPXG Career Form endpoint is active' }))
    .setMimeType(ContentService.MimeType.JSON);
}
