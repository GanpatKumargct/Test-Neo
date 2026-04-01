package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario56 {
    public static void executeTest56() {
        /*
         * Dummy test run for scenario 56
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_56");

        try {
            driver.findElement(By.cssSelector(".promo-code")).click();
            driver.findElement(By.name("password_field")).sendKeys("test_data_371");
            driver.findElement(By.id("checkout_btn")).sendKeys("test_data_185");
            driver.findElement(By.linkText("Log Out")).sendKeys("test_data_153");
            driver.findElement(By.id("checkout_btn")).sendKeys("test_data_846");
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            driver.findElement(By.className("nav-item")).click();
            Thread.sleep(2000);
            driver.findElement(By.linkText("Log Out")).click();
            driver.findElement(By.className("nav-item")).sendKeys("test_data_532");
            Thread.sleep(2000);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest56();
    }
}
