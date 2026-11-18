/*
 * Google Apps Script — Contact Form Handler
 * 
 * INSTRUCTIONS:
 * 1. Open your Google Sheet
 * 2. Go to Extensions → Apps Script
 * 3. Delete all existing code and paste this entire file
 * 4. Save, then Deploy → New deployment → Web app
 *    - Execute as: Me
 *    - Who has access: Anyone
 * 5. Copy the deployed URL and paste it into script.js
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
    
    // Append a new row with the form data
    sheet.appendRow([
      new Date(),          // Timestamp
      data.name,           // Full Name
      data.email,          // Email
      data.phone,          // Contact Number
      data.message,        // Message
      data.service         // Service Interest
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
    .createTextOutput(JSON.stringify({ status: 'ok', message: 'SAPXG Contact Form endpoint is active' }))
    .setMimeType(ContentService.MimeType.JSON);
}
