const fs = require('fs');
const path = require('path');

module.exports.onCapturePublishData = fs.readFileSync(path.join(__dirname, 'onCapturePublishData.gql'), 'utf8');
module.exports.onIotPublish = fs.readFileSync(path.join(__dirname, 'onIotPublish.gql'), 'utf8');
module.exports.onNotifyCaptureComplete = fs.readFileSync(path.join(__dirname, 'onNotifyCaptureComplete.gql'), 'utf8');
module.exports.onNotifyIotQueryExportComplete = fs.readFileSync(path.join(__dirname, 'onNotifyIotQueryExportComplete.gql'), 'utf8');
module.exports.onNotifyTimeSeriesQueryExportComplete = fs.readFileSync(path.join(__dirname, 'onNotifyTimeSeriesQueryExportComplete.gql'), 'utf8');
module.exports.onNotifyUploadComplete = fs.readFileSync(path.join(__dirname, 'onNotifyUploadComplete.gql'), 'utf8');
module.exports.onStartCapture = fs.readFileSync(path.join(__dirname, 'onStartCapture.gql'), 'utf8');
module.exports.onStopCapture = fs.readFileSync(path.join(__dirname, 'onStopCapture.gql'), 'utf8');
module.exports.onTimeSeriesDbPublish = fs.readFileSync(path.join(__dirname, 'onTimeSeriesDbPublish.gql'), 'utf8');
