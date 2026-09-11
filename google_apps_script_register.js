// Google Apps Script for Registration form with CV upload to Google Drive
// Paste this in your Google Sheet's Apps Script editor
// (Extensions → Apps Script)
// IMPORTANT: After pasting, Deploy → Manage deployments → Edit → New Version → Deploy

function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    var cvLink = '';
    
    // If a file was uploaded (sent as base64)
    if (data.fileData && data.fileName) {
      var decoded = Utilities.base64Decode(data.fileData);
      var blob = Utilities.newBlob(decoded, data.fileType || 'application/pdf', data.fileName);
      
      // Save to Google Drive (creates a folder called "SAPXG_CVs" if it doesn't exist)
      var folders = DriveApp.getFoldersByName('SAPXG_CVs');
      var folder;
      if (folders.hasNext()) {
        folder = folders.next();
      } else {
        folder = DriveApp.createFolder('SAPXG_CVs');
      }
      
      var file = folder.createFile(blob);
      file.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
      cvLink = file.getUrl();
    }
    
    var techString = data.technologies || '';
    var hasSAC = techString.includes('SAC') ? 'X' : '';
    var hasDatasphere = techString.includes('DATASPHERE') ? 'X' : '';
    var hasBIBW = techString.includes('BI/BW') ? 'X' : '';
    var hasHANA = techString.includes('HANA') ? 'X' : '';
    
    sheet.appendRow([
      data.fullname || '',       // A: Name
      data.email || '',          // B: Email
      data.phone || '',          // C: Contact Number
      data.totalexp || '',       // D: Total Experience
      data.relevantexp || '',    // E: Relevant Experience
      data.projects || '',       // F: Number of projects completed in relevant platform
      cvLink,                    // G: CV Upload (Google Drive link)
      new Date(),                // H: Timestamp
      hasSAC,                    // I: SAC
      hasDatasphere,             // J: DATASPHERE
      hasBIBW,                   // K: BI/BW
      hasHANA                    // L: HANA
    ]);
    
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'success', cvLink: cvLink }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ status: 'error', message: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
