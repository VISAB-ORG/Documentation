# Setup
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

**Running the application**
1. Clone the repository using HTTPS `git clone https://github.com/VISAB-ORG/VISAB.git`.
2. Run `mvn compile`
3. Configure `org.visab.main.Main` to be the target of your run configuration.

You can now run VISAB from your IDE.

## Developing VISABConnector and VISABConnector.Unity
.Net Framework 4.8 [Developer Pack](https://dotnet.microsoft.com/download/dotnet-framework/net48) and a C# IDE (Visual Studio, Visual Studio Code, ...) are prequisites for developing VISABConnector and VISABConnector.Unity.

**Building the assemblies**
1. Clone the repository using HTTPS `git clone https://github.com/VISAB-ORG/VISABConnector.git`.
2. Open the solution file at src/VISABConnector.sln
3. Build the solution using your IDE

The compiled assemblies appear in the bin/ directory of the project directories.

## Developing the Unity games
If you want to further develop the Unity games or change what data is transmitted from the games to VISAB you need [Unity 2021.1.1](https://unity3d.com/de/unity/whats-new/2021.1.1).
Afterwards you can simply open the game projects using the Unity Editor.