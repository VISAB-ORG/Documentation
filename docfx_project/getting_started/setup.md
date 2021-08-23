# Environment Setup
VISABs source control is done using Git and a remote repository is hosted on [GitHub](https://github.com/VISAB-ORG/VISAB). Releases of VISAB include both the jar and the source files. Download the latest version from [here](https://github.com/VISAB-ORG/VISAB/releases).

## Installing VISAB
A JRE version equal or greater than Java 11 is required for using VISAB.
If that requirement is satisfied you can start VISAB from your shell in two modes.

**GUI**
This mode provides features for visualizing game data files and starts the HTTP API for reciving data.\
`java -jar VISAB.jar -mode gui`

**Headless**
This mode only starts the HTTP API for reciving data.\
`java -jar VISAB.jar -mode headless`

## Developing VISAB
A JDK version equal or greater than Java 11 and [Maven](https://maven.apache.org/) are prequisites for developing VISAB.
