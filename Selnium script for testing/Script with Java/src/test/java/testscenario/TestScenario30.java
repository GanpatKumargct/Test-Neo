package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario30 {
    public static void executeTest30() {
        /*
         * Dummy test run for scenario 30
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_30");

        try {
            driver.findElement(By.cssSelector(".promo-code")).click();
            driver.findElement(By.linkText("Log Out")).sendKeys("test_data_799");
            driver.findElement(By.xpath("//button[@type='submit']")).sendKeys("test_data_159");
            driver.findElement(By.id("checkout_btn")).sendKeys("test_data_852");
            Thread.sleep(2000);
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            driver.findElement(By.name("password_field")).sendKeys("test_data_892");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest30();
    }
}
