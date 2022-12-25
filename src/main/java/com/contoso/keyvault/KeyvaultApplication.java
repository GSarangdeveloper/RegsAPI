package com.contoso.keyvault;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;

@SpringBootApplication
@RestController
public class KeyvaultApplication implements CommandLineRunner {
    @Value("${DBUSER3}")
    private String connectionString ;

    public static void main(String[] args) {
        SpringApplication.run(KeyvaultApplication.class, args);
    }

    @GetMapping("get")
    public String get() {
        return connectionString;
    }

    public void run(String... varl) throws Exception {
        System.out.println(String.format("\nConnection String stored in Azure Key Vault:\n%s\n",connectionString));
    }

}
