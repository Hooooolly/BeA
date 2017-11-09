from mininet.topo import Topo

class MyTopo( Topo ):

	def __init__( self ):
		
		Topo.__init__( self )

		leftSwitch = self.addSwitch( 's1' )
		rightSwitch = self.addSwitch( 's2' )
		firstHost = self.addHost ( 'h1' )
		secondHost = self.addHost ( 'h2' )
		thirdHost = self.addHost ( 'h3' )
		fourthHost = self.addHost ( 'h4' )

		self.addLink ( firstHost, leftSwitch )
		self.addLink ( secondHost, leftSwitch )
		self.addLink ( thirdHost, leftSwitch )
		self.addLink ( fourthHost, rightSwitch )
		self.addLink ( rightSwitch, leftSwitch )

topos = { 'mytopo': ( lambda: MyTopo() ) }
