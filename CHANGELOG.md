[//]: # ( This is a comment )

[//]: # ( Use format below to add a new release entry. )
[//]: # ( Releases are sorted newest to oldest )
[//]: # ( Add the release comparison url at the bottom of the file )

[//]: # ( ## [New Release version] - yyyy-mm-dd )
[//]: # ( ### Added )
[//]: # ( - list new features )
[//]: # ( ### Changed )
[//]: # ( - list changes in existing functionality )
[//]: # ( ### Deprecated )
[//]: # ( - list soon-to-be removed features )
[//]: # ( ### Removed )
[//]: # ( - list features that have been removed )
[//]: # ( ### Fixed )
[//]: # ( - list bug fixes )
[//]: # ( ### Security )
[//]: # ( - list any vulnerabilities )

# Avista Digital Exchange SDK Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.6] - 2024-01-18

### Fixed

- Updated the required python version. Earlier versions were failing due to typing.

## [0.3.5] - 2024-01-17

### Fixed

- Changed dict access from [] to .get() for function in GraphQLClientGraphQLError Exception type

## [0.3.3] - 2023-07-18

### Fixed

- Fixed websocket package dependency issues.
- Fixed other package dependencies.

### Added

- Added support for ariadne-codegen generated async graphql client. Modified the client to use the correct websocket protocol and get around some errors.
- Added method for subscribing to data capture data updates.

## [0.3.0] - 2023-06-15

### Added

- Added new method for generating a graphql client and python types from a graphql schema.
- Added new Data Capture module with publishData, startCapture, and stopCapture commands.

## [0.2.1] - 2023-02-15

### Fixed

- Fixed description issue in createEndpoint.

## [0.2.0] - 2023-02-14

### Fixed

- Fixed description issue in createModel.
- Added a missing comma in createModel example in the README.
- Removed spaces from model name in the createModel example in the README.

## [0.1.5] - 2023-01-25

### Added

- Ability to create a new iot endpoint (iot.createEndpoint)
- Ability to create a digital twin model (iot.createModel)

### Fixed

- README markdown section references not working in PyPi viewer. Added HTML tags at each section header to support scrolling to an id. It is a known [readme_renderer issue](https://github.com/pypa/readme_renderer/issues/169).

## [0.1.4] - 2022-12-21

### Fixed

- Fixed file download error.

## [0.1.3] - 2022-12-19

### Added

- Added ISO8601 as a time unit option for publishing iot data.

### Fixed

- Fixed query return type for data store files and directories (owner replaced by ownerUserId).

## [0.1.2] - 2022-12-13

### Changed

- Updated data format for publishing iot attribute data ('name': 'value').
- Now allow ISO 8601 timestamps for querying iot data by time range.

## [0.1.1] - 2022-12-09

### Fixed

- Pointed to production api endpoint.

## [0.1.0] - 2022-12-09

### Added

- IoT Service features - getEndpoint, listEndpointLastValues, queryByTimeRange, publish, and updateEndpointProperties.

### Removed

- TimeSeries features.
- Collaborative features.

## [0.0.24] - 2022-10-05

### Added

- Added file system commands to DataStore object (cd, ls, pwd, uploadFile, downloadFile, deleteFile).
- Started a simpler publishToDatabase (time series) but not usable yet.

### Fixed

- Fixed list all assets and their attributes to use nextToken if received.

## [0.0.23] - 2022-09-29

### Added

- Added query to list all the assets and their attributes in a time series database, along with all attribute's latest value.
- Added a structured time series query to allow for querying with a time range, and asset and attribute filter.

### Changed

- Improved print statements.

### Fixed

- Fixed debug variable access.

## [0.0.22] - 2022-09-16

### Changed

- Updated README

### Fixed

- Fixed time series querying
- Fixed debug mode

## [0.0.21] - 2022-09-15

### Changed

- Changed a few print statments to be conditional with `if debug`

### Fixed
- Fixed function relative imports

## [0.0.20] - 2022-09-16

### Changed

- Changed all `self.client` to `self._client`
- Changed a few print statments to be conditional with `if debug`

### Removed

- Removed access to AvistaDigitalExchange's member variable `client`.  
  
## 0.0.19 - 2022-09-15

Missing a git commit to pin this to.

### Changed

- Changed API url to point at production environment.
- Updated CHANGELOG format.
- Minor updates to README.

## [0.0.18] - 2022-09-13

First Beta-ready release.

### Added
- Added programmatic access to the Avista Digital Exchange.
- Added beta features that are ready for testing:
     - getUserInfo
     - listDataStores
     - getDataStore
     - getDataStoreDirectory
     - getDataStoreFileMeta
     - downloadDataStoreFile
     - uploadFileToDataStore
     - deleteDataStoreFile
     - listTimeSeriesDatabases
     - getTimeSeriesDatabase
     - queryTimeSeriesDatabaseWithTimestreamFormat
     - createTimeSeriesMeasureValue
     - createTimeSeriesDimension
     - createTimeSeriesInputRecord
     - publishToTimeSeriesDatabase
     - listCollaboratives
     - getCollaborative
     - listCollaborativeServices
     - listCollaborativesServiceSharedWith
     - addServiceToCollaborative
     - removeServiceFromCollaborative

[Unreleased]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2024_01_18_v0.3.6...HEAD
[0.3.5]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2024_01_17_v0.3.5...release/2024_01_18_v0.3.6
[0.3.5]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2023_07_18_v0.3.3...release/2024_01_17_v0.3.5
[0.3.3]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2023_06_15_v0.3.0...release/2023_07_18_v0.3.3
[0.3.0]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2023_02_15_v0.2.1...release/2023_06_15_v0.3.0
[0.2.1]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2023_02_14_v0.2.0...release/2023_02_15_v0.2.1
[0.2.0]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_12_25_v0.1.5...release/2023_02_14_v0.2.0
[0.1.5]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_12_21_v0.1.4...release/2023_01_25_v0.1.5
[0.1.4]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_12_19_v0.1.3...release/2022_12_21_v0.1.4
[0.1.3]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_12_13_v0.1.2...release/2022_12_19_v0.1.3
[0.1.2]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_12_09_v0.1.1...release/2022_12_13_v0.1.2
[0.1.1]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_12_09_v0.1.0...release/2022_12_09_v0.1.1
[0.1.0]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_09_29_v0.0.24...release/2022_12_09_v0.1.0
[0.0.24]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_09_29_v0.0.23...release/2022_09_29_v0.0.24
[0.0.23]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_09_16_v0.0.22...release/2022_09_29_v0.0.23
[0.0.22]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_09_15_v0.0.21...release/2022_09_16_v0.0.22
[0.0.21]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_09_15_v0.0.20...release/2022_09_15_v0.0.21
[0.0.20]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_09_13_v0.0.18...release/2022_09_15_v0.0.20
[0.0.19]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_09_13_v0.0.18...release/2022_09_15_v0.0.20
[0.0.18]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/tree/release/2022_09_13_v0.0.18
