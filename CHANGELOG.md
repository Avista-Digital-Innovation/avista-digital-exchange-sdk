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
[//]: # ( ### Fixed for )
[//]: # ( - list bug fixes )
[//]: # ( ### Security )
[//]: # ( - list any vulnerabilities )

# Avista Digital Exchange SDK Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

[Unreleased]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_09_29_v0.0.23...HEAD
[0.0.23]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_09_16_v0.0.22...release/2022_09_29_v0.0.23
[0.0.22]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_09_15_v0.0.21...release/2022_09_16_v0.0.22
[0.0.21]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_09_15_v0.0.20...release/2022_09_15_v0.0.21
[0.0.20]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_09_13_v0.0.18...release/2022_09_15_v0.0.20
[0.0.19]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_09_13_v0.0.18...release/2022_09_15_v0.0.20
[0.0.18]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/tree/release/2022_09_13_v0.0.18
