
## Press Release

The storage infrastructure that supports the Devolo requires monitoring, which led the purchasing of SANView.  This tool, is not giving he storge team the level of control and detail of the management and monitoring of their devices, as such they have decided to implement _DUCKView_. LThe advantages of this project over SANView is the level of control over data gathered, and customisation of how reporting can and will be achieved.

The Storage team will overcome the cons of the existing system by working to deliver an reporting tool that will:

- ingest the captured operational information of an existing device
- process the information extracting key data
- save this data in a database
- incorporate the saved data into standard reports that will allow for system health checks in a structured and repeatable manner
- compare new data against historical data and display differences.

## FAQ

### What are the basic components of the system?

The basic components of the system are, a **RESTful API call/parser** to a target device, a **state database**, and a **reporting engine**. These components are all provided by the Devolo Storage Team/[psmware ltd.](https://psmware.ie)

### What is the RESTful API call/parser?

Each device managed byt the Storage Team provides a RESTful API to allow the device to be interrogated for information. These APIs will be accessed to gather operational information about each device.  The responses sent by each device will be parsed to glean the required operational data, ready for importing into the **state database**.

### What is the state database?

The state database is a source of record for the operational state of the storage devices as captured. This allows for daily operation health check reporting,  and for the configuration drift reporting, when compared against the historical data. The data model must be able to maintain historical state for specific settings that will apply to all devices.

### What is the reporting engine?

The reporting engine will be an automated ETL that will process new entries into the state database, and build operational report roll-up data to be used by daily health-check reporting. And report where operational data has changed from previously captured data.  I.e. a new disk is added to a host an SVC, or a new port is active on a fabric switch.

## Automation Workflows

**How are the basic workflows organised?**

Each workflow stage will be activated via cron tasks

### Capture

- make a GET call to REST API of a device
- gather the output of the response
- parse the output, and store data in the loading tables of the state database

### Processing

- Start ETL process to extract data from loading tables
- process loading tables
- build roll-up reporting tables for health check analysis
- build configuration change tables for reporting devices changes
- clear loading tables once complete

### Reporting

- Send health-chek reports to required team
- Send configuration drift reports to required team

### Repository

[GitHub](https://github.com/b-skwad/duckview)

### Development Environment

[Self Contained Dev Environment(SCDE)](cdf/prerequisites.md)

### Environment Variables

TBD

### Database Configuration

Deploy State Database on [MySQL](https://hub.docker.com/_/mysql)
