Feature: Blocking all traffic on a given network

        Scenario: Blocking Traffic
                Given There is incoming traffic
                When A dangerous IP is detected
                Then Block traffic


