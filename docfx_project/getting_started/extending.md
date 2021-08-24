# Extending VISAB for a new game
<p>The underlying code base of VISAB is designed to be easily extensible.<br>
This article will guide you through all relevant changes you need to perform, <br>
if you desire to make VISAB capable of supporting a new game.<br>
As the below order already indicates, we advise you to start with the modifications<br>
in your game, because then you will have a fixed basis, of what shall be processed within VISAB.</p>

### Short overview of actions to be performed
<ol>
	<li>Deploy the <code>VISABConnector</code> in your (Unity-) game</li>
	<li>Create a statistics POJO in the game.</li>
	<li>Implement a <code>VISABHelper</code> in your (Unity-) game</li>
	<li>[OPTIONAL] Use the <code>VISABConnector.Unity</code> to perform snapshots</li>
	<li>Create a new <code>SessionListener</code> in VISAB</li>
	<li>Create a statistics POJO in VISAB.</li>
	<li>Create a <code>VISABFile</code> in VISAB</li>
	<li>Implement desired visualizers for your (Unity-) game</li>
	<ul>
		<li>Create a Meta-View</li>
		<li>Create a Statistics-View</li>
		<li>Create a Replay View</li>
		<li>Create any other View you find helpful</li>
	</ul>
</ol>