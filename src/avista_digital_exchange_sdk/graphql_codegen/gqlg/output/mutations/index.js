const fs = require('fs');
const path = require('path');

module.exports.collaborative_addServiceToCollaborative = fs.readFileSync(path.join(__dirname, 'collaborative_addServiceToCollaborative.gql'), 'utf8');
module.exports.collaborative_removeServiceFromCollaborative = fs.readFileSync(path.join(__dirname, 'collaborative_removeServiceFromCollaborative.gql'), 'utf8');
module.exports.collaborative_updateCollaborativeMemberOrganization = fs.readFileSync(path.join(__dirname, 'collaborative_updateCollaborativeMemberOrganization.gql'), 'utf8');
module.exports.dataCapture_attachFile = fs.readFileSync(path.join(__dirname, 'dataCapture_attachFile.gql'), 'utf8');
module.exports.dataCapture_createCapture = fs.readFileSync(path.join(__dirname, 'dataCapture_createCapture.gql'), 'utf8');
module.exports.dataCapture_deleteAttachment = fs.readFileSync(path.join(__dirname, 'dataCapture_deleteAttachment.gql'), 'utf8');
module.exports.dataCapture_deleteCapture = fs.readFileSync(path.join(__dirname, 'dataCapture_deleteCapture.gql'), 'utf8');
module.exports.dataCapture_handleCompletion = fs.readFileSync(path.join(__dirname, 'dataCapture_handleCompletion.gql'), 'utf8');
module.exports.dataCapture_notifyCaptureComplete = fs.readFileSync(path.join(__dirname, 'dataCapture_notifyCaptureComplete.gql'), 'utf8');
module.exports.dataCapture_publishData = fs.readFileSync(path.join(__dirname, 'dataCapture_publishData.gql'), 'utf8');
module.exports.dataCapture_regenerateAuthenticationToken = fs.readFileSync(path.join(__dirname, 'dataCapture_regenerateAuthenticationToken.gql'), 'utf8');
module.exports.dataCapture_startCapture = fs.readFileSync(path.join(__dirname, 'dataCapture_startCapture.gql'), 'utf8');
module.exports.dataCapture_stopCapture = fs.readFileSync(path.join(__dirname, 'dataCapture_stopCapture.gql'), 'utf8');
module.exports.dataCapture_updateCapture = fs.readFileSync(path.join(__dirname, 'dataCapture_updateCapture.gql'), 'utf8');
module.exports.dataCapture_updateDataModel = fs.readFileSync(path.join(__dirname, 'dataCapture_updateDataModel.gql'), 'utf8');
module.exports.dataCapture_uploadDataModelFile = fs.readFileSync(path.join(__dirname, 'dataCapture_uploadDataModelFile.gql'), 'utf8');
module.exports.iot_addEndpointsToGroup = fs.readFileSync(path.join(__dirname, 'iot_addEndpointsToGroup.gql'), 'utf8');
module.exports.iot_cancelQuery = fs.readFileSync(path.join(__dirname, 'iot_cancelQuery.gql'), 'utf8');
module.exports.iot_createEndpoint = fs.readFileSync(path.join(__dirname, 'iot_createEndpoint.gql'), 'utf8');
module.exports.iot_createGroup = fs.readFileSync(path.join(__dirname, 'iot_createGroup.gql'), 'utf8');
module.exports.iot_createHub = fs.readFileSync(path.join(__dirname, 'iot_createHub.gql'), 'utf8');
module.exports.iot_createModel = fs.readFileSync(path.join(__dirname, 'iot_createModel.gql'), 'utf8');
module.exports.iot_createNewModelVersion = fs.readFileSync(path.join(__dirname, 'iot_createNewModelVersion.gql'), 'utf8');
module.exports.iot_deleteEndpoint = fs.readFileSync(path.join(__dirname, 'iot_deleteEndpoint.gql'), 'utf8');
module.exports.iot_deleteGroup = fs.readFileSync(path.join(__dirname, 'iot_deleteGroup.gql'), 'utf8');
module.exports.iot_deleteHub = fs.readFileSync(path.join(__dirname, 'iot_deleteHub.gql'), 'utf8');
module.exports.iot_deleteModel = fs.readFileSync(path.join(__dirname, 'iot_deleteModel.gql'), 'utf8');
module.exports.iot_generateQueryResultExport = fs.readFileSync(path.join(__dirname, 'iot_generateQueryResultExport.gql'), 'utf8');
module.exports.iot_notifyQueryExportComplete = fs.readFileSync(path.join(__dirname, 'iot_notifyQueryExportComplete.gql'), 'utf8');
module.exports.iot_publish = fs.readFileSync(path.join(__dirname, 'iot_publish.gql'), 'utf8');
module.exports.iot_regenerateEndpointToken = fs.readFileSync(path.join(__dirname, 'iot_regenerateEndpointToken.gql'), 'utf8');
module.exports.iot_removeEndpointsFromGroup = fs.readFileSync(path.join(__dirname, 'iot_removeEndpointsFromGroup.gql'), 'utf8');
module.exports.iot_updateEndpoint = fs.readFileSync(path.join(__dirname, 'iot_updateEndpoint.gql'), 'utf8');
module.exports.iot_updateEndpointProperties = fs.readFileSync(path.join(__dirname, 'iot_updateEndpointProperties.gql'), 'utf8');
module.exports.iot_updateGroup = fs.readFileSync(path.join(__dirname, 'iot_updateGroup.gql'), 'utf8');
module.exports.iot_updateHub = fs.readFileSync(path.join(__dirname, 'iot_updateHub.gql'), 'utf8');
module.exports.iot_updateModel = fs.readFileSync(path.join(__dirname, 'iot_updateModel.gql'), 'utf8');
module.exports.iot_updateModelUsedByEndpoint = fs.readFileSync(path.join(__dirname, 'iot_updateModelUsedByEndpoint.gql'), 'utf8');
module.exports.notifications_notifyUploadComplete = fs.readFileSync(path.join(__dirname, 'notifications_notifyUploadComplete.gql'), 'utf8');
module.exports.platformAdmin_addCollaborativeMember = fs.readFileSync(path.join(__dirname, 'platformAdmin_addCollaborativeMember.gql'), 'utf8');
module.exports.platformAdmin_createCollaborative = fs.readFileSync(path.join(__dirname, 'platformAdmin_createCollaborative.gql'), 'utf8');
module.exports.platformAdmin_createOrganization = fs.readFileSync(path.join(__dirname, 'platformAdmin_createOrganization.gql'), 'utf8');
module.exports.platformAdmin_createUser = fs.readFileSync(path.join(__dirname, 'platformAdmin_createUser.gql'), 'utf8');
module.exports.platformAdmin_deleteCollaborative = fs.readFileSync(path.join(__dirname, 'platformAdmin_deleteCollaborative.gql'), 'utf8');
module.exports.platformAdmin_deleteOrganization = fs.readFileSync(path.join(__dirname, 'platformAdmin_deleteOrganization.gql'), 'utf8');
module.exports.platformAdmin_deleteUser = fs.readFileSync(path.join(__dirname, 'platformAdmin_deleteUser.gql'), 'utf8');
module.exports.platformAdmin_deleteUsersCollaboratives = fs.readFileSync(path.join(__dirname, 'platformAdmin_deleteUsersCollaboratives.gql'), 'utf8');
module.exports.platformAdmin_deleteUsersServices = fs.readFileSync(path.join(__dirname, 'platformAdmin_deleteUsersServices.gql'), 'utf8');
module.exports.platformAdmin_migrateUsersCollaborativesOwnership = fs.readFileSync(path.join(__dirname, 'platformAdmin_migrateUsersCollaborativesOwnership.gql'), 'utf8');
module.exports.platformAdmin_migrateUsersServicesOwnership = fs.readFileSync(path.join(__dirname, 'platformAdmin_migrateUsersServicesOwnership.gql'), 'utf8');
module.exports.platformAdmin_removeCollaborativeMember = fs.readFileSync(path.join(__dirname, 'platformAdmin_removeCollaborativeMember.gql'), 'utf8');
module.exports.platformAdmin_resendUserInvitation = fs.readFileSync(path.join(__dirname, 'platformAdmin_resendUserInvitation.gql'), 'utf8');
module.exports.platformAdmin_updateCollaborative = fs.readFileSync(path.join(__dirname, 'platformAdmin_updateCollaborative.gql'), 'utf8');
module.exports.platformAdmin_updateCollaborativeMember = fs.readFileSync(path.join(__dirname, 'platformAdmin_updateCollaborativeMember.gql'), 'utf8');
module.exports.platformAdmin_updateOrganization = fs.readFileSync(path.join(__dirname, 'platformAdmin_updateOrganization.gql'), 'utf8');
module.exports.platformAdmin_updateUser = fs.readFileSync(path.join(__dirname, 'platformAdmin_updateUser.gql'), 'utf8');
module.exports.storage_createDataStore = fs.readFileSync(path.join(__dirname, 'storage_createDataStore.gql'), 'utf8');
module.exports.storage_createDataStoreDirectory = fs.readFileSync(path.join(__dirname, 'storage_createDataStoreDirectory.gql'), 'utf8');
module.exports.storage_createDataStoreFile = fs.readFileSync(path.join(__dirname, 'storage_createDataStoreFile.gql'), 'utf8');
module.exports.storage_createDataStoreFileDataView = fs.readFileSync(path.join(__dirname, 'storage_createDataStoreFileDataView.gql'), 'utf8');
module.exports.storage_deleteDataStore = fs.readFileSync(path.join(__dirname, 'storage_deleteDataStore.gql'), 'utf8');
module.exports.storage_deleteDataStoreDirectory = fs.readFileSync(path.join(__dirname, 'storage_deleteDataStoreDirectory.gql'), 'utf8');
module.exports.storage_deleteDataStoreFile = fs.readFileSync(path.join(__dirname, 'storage_deleteDataStoreFile.gql'), 'utf8');
module.exports.storage_deleteDataStoreFileDataView = fs.readFileSync(path.join(__dirname, 'storage_deleteDataStoreFileDataView.gql'), 'utf8');
module.exports.storage_updateDataStore = fs.readFileSync(path.join(__dirname, 'storage_updateDataStore.gql'), 'utf8');
module.exports.storage_updateDataStoreDirectory = fs.readFileSync(path.join(__dirname, 'storage_updateDataStoreDirectory.gql'), 'utf8');
module.exports.storage_updateDataStoreFile = fs.readFileSync(path.join(__dirname, 'storage_updateDataStoreFile.gql'), 'utf8');
module.exports.timeSeriesDb_cancelDatabaseQuery = fs.readFileSync(path.join(__dirname, 'timeSeriesDb_cancelDatabaseQuery.gql'), 'utf8');
module.exports.timeSeriesDb_createDatabase = fs.readFileSync(path.join(__dirname, 'timeSeriesDb_createDatabase.gql'), 'utf8');
module.exports.timeSeriesDb_deleteDatabase = fs.readFileSync(path.join(__dirname, 'timeSeriesDb_deleteDatabase.gql'), 'utf8');
module.exports.timeSeriesDb_generateQueryResultExportFile = fs.readFileSync(path.join(__dirname, 'timeSeriesDb_generateQueryResultExportFile.gql'), 'utf8');
module.exports.timeSeriesDb_notifyTimeSeriesQueryExportComplete = fs.readFileSync(path.join(__dirname, 'timeSeriesDb_notifyTimeSeriesQueryExportComplete.gql'), 'utf8');
module.exports.timeSeriesDb_publishToDatabase = fs.readFileSync(path.join(__dirname, 'timeSeriesDb_publishToDatabase.gql'), 'utf8');
module.exports.timeSeriesDb_updateDatabase = fs.readFileSync(path.join(__dirname, 'timeSeriesDb_updateDatabase.gql'), 'utf8');
module.exports.user_createAuthenticationToken = fs.readFileSync(path.join(__dirname, 'user_createAuthenticationToken.gql'), 'utf8');
module.exports.user_deleteAuthenticationToken = fs.readFileSync(path.join(__dirname, 'user_deleteAuthenticationToken.gql'), 'utf8');
