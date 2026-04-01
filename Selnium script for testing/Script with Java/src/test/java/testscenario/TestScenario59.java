package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario59 {
    public static void executeTest59() {
        /*
         * Dummy test run for scenario 59
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_59");

        try {
            driver.findElement(By.xpath("//button[@type='submit']")).sendKeys("test_data_483");
            if (!driver.findElement(By.cssSelector(".promo-code")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            driver.findElement(By.id("user_name")).sendKeys("test_data_314");
            if (!driver.findElement(By.xpath("//button[@type='submit']")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.cssSelector(".promo-code")).sendKeys("test_data_469");
            driver.findElement(By.linkText("Log Out")).sendKeys("test_data_454");
            driver.findElement(By.id("checkout_btn")).click();
            driver.findElement(By.className("nav-item")).sendKeys("test_data_129");
            Thread.sleep(2000);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest59();
    }
}
