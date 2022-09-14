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

## [Unreleased] - WIP

[//]: # ( Provide info on changes that will be a part of the next release )

## [0.0.19] - 2022-09-14

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




[Unreleased]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/compare/release/2022_09_14_v0.0.19...HEAD
[0.0.19]: https://github.com/olivierlacan/keep-a-changelog/compare/2022_09_13_v0.0.18...2022_09_14_v0.0.19
[0.0.18]: https://github.com/Avista-Digital-Innovation/avista-digital-exchange-sdk/tree/release/2022_09_13_v0.0.18
