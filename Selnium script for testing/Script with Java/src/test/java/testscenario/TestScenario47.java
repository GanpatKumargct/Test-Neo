package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario47 {
    public static void executeTest47() {
        /*
         * Dummy test run for scenario 47
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_47");

        try {
            driver.findElement(By.cssSelector(".promo-code")).click();
            if (!driver.findElement(By.linkText("Log Out")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.id("user_name")).click();
            driver.findElement(By.xpath("//button[@type='submit']")).sendKeys("test_data_136");
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            driver.findElement(By.linkText("Log Out")).sendKeys("test_data_210");
            Thread.sleep(2000);
            driver.findElement(By.linkText("Log Out")).sendKeys("test_data_759");
            driver.findElement(By.cssSelector(".promo-code")).click();
            driver.findElement(By.linkText("Log Out")).sendKeys("test_data_468");
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest47();
    }
}
