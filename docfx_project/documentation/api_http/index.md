# HTTP API Endpoints
VISAB has a HTTP based API for reciving data from games.
The [WebAPI](xref:org.visab.api.WebAPI) is implemented as a `RouterNanoHTTPD` of the [nanohttpd](https://github.com/NanoHttpd/nanohttpd) library. Below you find documentation of the various endpoints exposed by the API.

## Ping Endpoint
A simple ping endpoint to check if VISAB is running.

|Request method|Endpoint|Parameters|Description|Response|
|-|-|-|-|-|
|GET| /ping | - | Pings VISAB. | A simple arbitrary response message. |

## Session Endpoint
Anything transmission session related.

|Request method|Endpoint|Parameters|Description|Response|
|-|-|-|-|-|
|POST| /session/open | **Body** A json string representing the [IMetaInformation](xref:org.visab.globalmodel.IMetaInformation) object. | Opens a transmission session. | A UUID string identifying the tranmission session. |
|GET| /session/close | **Header** The key `sessionid` contains a string of the UUID of the transmission session to close. | Closes a transmission session. | Simple response message. |
|GET| /session/status | **Query string** The key `sessionid` contains the UUID of the transmission session to get the status of. | Gets the status of a transmission session. | A json string representing of the [SessionStatus](xref:org.visab.globalmodel.SessionStatus) of the transmission session. |
|GET| /session/list | - | Gets the statuses of all active transmission session. | A json string representing an array of the [SessionStatus](xref:org.visab.globalmodel.SessionStatus) for all active tranmission sessions. |

## Sending Data Endpoint
Anything related to sending statistics and image data.

|Request method|Endpoint|Parameters|Description|Response|
|-|-|-|-|-|
|POST| /send/statistics | **Body** A json string representing the [IStatistics](xref:org.visab.globalmodel.IStatistics) object. <br/> **Header** The key `sessionid` contains a string of the UUID of the transmission session from which data is sent. The key `game` contains a string of the name of the game of the transmission session. | Sends statistics for VISAB to process. | If the session was active a simple response message is returnd, otherwise "SESSION_ALREADY_CLOSED". |
|POST| /send/image | **Body** A json string representing the [IImageContainer](xref:org.visab.globalmodel.IImageContainer) object. <br/> **Header** The key `sessionid` contains a string of the UUID of the transmission session from which data is sent. The key `game` contains a string of the name of the game of the transmission session. | Sends images for VISAB to process. | If the session was active a simple response message is returnd, otherwise "SESSION_ALREADY_CLOSED". |

## Game Endpoint
An endpoint for getting the games supported according to the users settings.

|Request method|Endpoint|Parameters|Description|Response|
|-|-|-|-|-|
|GET| /games | - | Gets a list of all the games supported according to the user settings. | A json string representing an array of the game strings that are allowed. |

## File Endpoint
Anything related to VISAB files.

|Request method|Endpoint|Parameters|Description|Response|
|-|-|-|-|-|
|GET| /file/get | **Query string** The key `sessionid` contains the UUID of the transmission session to get the created file of. | Gets the json string of the VISAB file that was created for the tranmission session. | A json string representing the [IVISABFile](xref:org.visab.globalmodel.IVISABFile) object that was created for the tranmission session. |
|POST| /file/send | **Body** A json string representing the [IVISABFile](xref:org.visab.globalmodel.IVISABFile) to be saved in VISABs database. | Sends an existing VISAB file for VISAB to save in the database. | A simple response message. |