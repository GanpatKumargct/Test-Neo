package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario7 {
    public static void executeTest7() {
        /*
         * Dummy test run for scenario 7
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_7");

        try {
            driver.findElement(By.cssSelector(".promo-code")).click();
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            driver.findElement(By.xpath("//button[@type='submit']")).click();
            driver.findElement(By.className("nav-item")).click();
            Thread.sleep(2000);
            driver.findElement(By.className("nav-item")).sendKeys("test_data_362");
            if (!driver.findElement(By.id("user_name")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            driver.findElement(By.linkText("Log Out")).sendKeys("test_data_908");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest7();
    }
}
