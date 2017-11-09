Feature: Creating a simple switch between all hosts

        Scenario: Allowing all traffic
                Given There is incoming traffic
                When All traffic is coming from trusted sources
                Then Allow all traffic
