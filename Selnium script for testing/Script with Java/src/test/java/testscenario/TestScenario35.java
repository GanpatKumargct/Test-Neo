package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario35 {
    public static void executeTest35() {
        /*
         * Dummy test run for scenario 35
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_35");

        try {
            driver.findElement(By.xpath("//button[@type='submit']")).sendKeys("test_data_363");
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            Thread.sleep(2000);
            driver.findElement(By.xpath("//button[@type='submit']")).sendKeys("test_data_584");
            driver.findElement(By.id("user_name")).click();
            driver.findElement(By.xpath("//button[@type='submit']")).sendKeys("test_data_775");
            driver.findElement(By.className("nav-item")).sendKeys("test_data_684");
            driver.findElement(By.id("user_name")).sendKeys("test_data_933");
            driver.findElement(By.id("user_name")).sendKeys("test_data_733");
            Thread.sleep(2000);
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest35();
    }
}
