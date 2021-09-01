# Maintain Dynamic Class Mappings in VISAB

To ensure that VISAB is easily extensible without touching the given code base,<br>
the workflow is implemented in a reflection-based style which uses a class mapping for each game.

Below you can find a sample class mapping that already contains Tetris as well.

### classMapping.json

```json
[
    {
        "game": "CBRShooter",
        "metaInformation": "org.visab.globalmodel.cbrshooter.CBRShooterMetaInformation",
        "listener": "org.visab.processing.cbrshooter.CBRShooterListener",
        "statistics": "org.visab.globalmodel.cbrshooter.CBRShooterStatistics",
        "file": "org.visab.globalmodel.cbrshooter.CBRShooterFile",
        "image": "org.visab.globalmodel.cbrshooter.CBRShooterImages",
        "visualizer": "org.visab.gui.visualize.cbrshooter.view.CBRShooterMainView"
    },
    {
        "game": "Settlers",
        "metaInformation": "org.visab.globalmodel.settlers.SettlersMetaInformation",
        "listener": "org.visab.processing.settlers.SettlersListener",
        "statistics": "org.visab.globalmodel.settlers.SettlersStatistics",
        "file": "org.visab.globalmodel.settlers.SettlersFile",
        "image": "org.visab.globalmodel.settlers.SettlersImages",
        "visualizer": "org.visab.gui.visualize.settlers.view.SettlersMainView"
    },
	{
        "game": "Tetris",
        "metaInformation": "org.visab.globalmodel.tetris.TetrisMetaInformation",
        "listener": "org.visab.processing.tetris.TetrisListener",
        "statistics": "org.visab.globalmodel.tetris.TetrisStatistics",
        "file": "org.visab.globalmodel.tetris.TetrisFile",
        "image": "org.visab.globalmodel.tetris.TetrisImages",
        "visualizer": "org.visab.gui.visualize.tetris.view.TetrisMainView"
    }
]
```