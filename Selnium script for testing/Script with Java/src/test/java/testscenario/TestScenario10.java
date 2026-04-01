package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario10 {
    public static void executeTest10() {
        /*
         * Dummy test run for scenario 10
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_10");

        try {
            driver.findElement(By.className("nav-item")).sendKeys("test_data_805");
            driver.findElement(By.cssSelector(".promo-code")).sendKeys("test_data_898");
            if (!driver.findElement(By.name("password_field")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            driver.findElement(By.id("user_name")).click();
            if (!driver.findElement(By.id("checkout_btn")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.id("checkout_btn")).sendKeys("test_data_622");
            if (!driver.findElement(By.id("checkout_btn")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            Thread.sleep(2000);
            driver.findElement(By.id("user_name")).click();
            driver.findElement(By.id("checkout_btn")).sendKeys("test_data_508");
            driver.findElement(By.id("user_name")).sendKeys("test_data_579");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest10();
    }
}
