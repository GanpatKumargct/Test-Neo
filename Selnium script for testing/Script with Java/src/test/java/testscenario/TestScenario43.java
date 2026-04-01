package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario43 {
    public static void executeTest43() {
        /*
         * Dummy test run for scenario 43
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_43");

        try {
            Thread.sleep(2000);
            driver.findElement(By.cssSelector(".promo-code")).sendKeys("test_data_175");
            if (!driver.findElement(By.id("user_name")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.xpath("//button[@type='submit']")).click();
            driver.findElement(By.name("password_field")).sendKeys("test_data_325");
            driver.findElement(By.name("password_field")).sendKeys("test_data_193");
            driver.findElement(By.className("nav-item")).sendKeys("test_data_981");
            driver.findElement(By.id("user_name")).click();
            driver.findElement(By.xpath("//button[@type='submit']")).sendKeys("test_data_102");
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
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
        executeTest43();
    }
}
