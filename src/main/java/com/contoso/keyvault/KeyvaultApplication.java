package com.contoso.keyvault;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;


import com.azure.core.util.polling.SyncPoller;
import com.azure.identity.DefaultAzureCredential;
import com.azure.identity.DefaultAzureCredentialBuilder;
import com.azure.identity.ManagedIdentityCredential;
import com.azure.identity.ManagedIdentityCredentialBuilder;
import com.azure.security.keyvault.secrets.SecretClient;
import com.azure.security.keyvault.secrets.SecretClientBuilder;
import com.azure.security.keyvault.secrets.models.DeletedSecret;
import com.azure.security.keyvault.secrets.models.KeyVaultSecret;

@SpringBootApplication
@RestController
public class KeyvaultApplication implements CommandLineRunner {
  //  @Value("${Testing}")
  //  private String connectionString ;

    public static void main(String[] args) {
        SpringApplication.run(KeyvaultApplication.class, args);
    }

    @GetMapping("get")
   ManagedIdentityCredential managedIdentityCredential = new ManagedIdentityCredentialBuilder()
        .clientId("9ddc86fc-8e88-4f59-b266-798d8dc9d50e") // only required for user assigned
        .build();


    // Azure SDK client builders accept the credential as a parameter
    SecretClient client = new SecretClientBuilder()
        .vaultUrl("https://testreg1.vault.azure.net/")
        .credential(managedIdentityCredential)
        .buildClient();

        KeyVaultSecret retrievedSecret = client.getSecret("Testing");
        return retrievedSecret.getValue();
    }

    public void run(String... varl) throws Exception {
        System.out.println(String.format("\nConnection String stored in Azure Key Vault:\n%s\n",connectionString));
    }

}
