package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario44 {
    public static void executeTest44() {
        /*
         * Dummy test run for scenario 44
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_44");

        try {
            driver.findElement(By.linkText("Log Out")).sendKeys("test_data_173");
            driver.findElement(By.id("user_name")).sendKeys("test_data_731");
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            Thread.sleep(2000);
            driver.findElement(By.id("user_name")).sendKeys("test_data_403");
            driver.findElement(By.className("nav-item")).sendKeys("test_data_752");
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            driver.findElement(By.id("user_name")).sendKeys("test_data_808");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest44();
    }
}
