param dockerHubSourceImage string = 'kenhoover/testrepo:ken'

param containerGroupName string = 'testContainerGroup1'

param storageAccountName string
param managedIdentityName string = 'KentosoContainerImagesIdentity'
param inputContainerName string = 'input'
param outputContainerName string = 'output'

param cpuCount int = 1
param containerMemoryInGB int = 2

param logAnalyticsWorkspaceId string = 'ba334b8f-3187-4f68-837b-645393b2b81b'  // West US 3 sandbox LA workspace

@secure()
param logAnalyticsWorkspaceKey string


resource containerUserIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2018-11-30' existing = {
  name: managedIdentityName
}

resource containerGroup 'Microsoft.ContainerInstance/containerGroups@2021-03-01' = {
  name: containerGroupName
  location: resourceGroup().location
  tags: {}
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: {
      '${containerUserIdentity.id}': {}
    }
  }
  properties: {
    containers: [
      {
        name: 'container1'
        properties: {
          environmentVariables: [
            {
              name: 'STORAGEACCOUNTNAME'
              secureValue: storageAccountName
            }
            {
              name: 'INPUTCONTAINERNAME'
              value: inputContainerName
            }
            {
              name: 'OUTPUTCONTAINERNAME'
              value: outputContainerName
            }
          ]
          image: dockerHubSourceImage
          resources: {
            requests: {
              cpu: cpuCount
              memoryInGB: containerMemoryInGB
            }
          }
        }
      }
    ]
    diagnostics: {
      logAnalytics: {
        logType: 'ContainerInstanceLogs'
        workspaceId: logAnalyticsWorkspaceId
        workspaceKey: logAnalyticsWorkspaceKey
      }
    }
    osType: 'Linux'
    restartPolicy: 'Never'
    sku: 'Standard'
  }
}
