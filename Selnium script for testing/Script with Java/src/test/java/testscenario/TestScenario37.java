package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario37 {
    public static void executeTest37() {
        /*
         * Dummy test run for scenario 37
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_37");

        try {
            if (!driver.findElement(By.xpath("//button[@type='submit']")).isDisplayed()) {
                System.out.println("Element not displayed");
            }
            Thread.sleep(2000);
            driver.findElement(By.linkText("Log Out")).click();
            Thread.sleep(2000);
            driver.findElement(By.id("user_name")).sendKeys("test_data_628");
            Thread.sleep(2000);
            driver.findElement(By.id("user_name")).click();
            driver.findElement(By.className("nav-item")).click();
            driver.findElement(By.xpath("//button[@type='submit']")).click();
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            driver.findElement(By.name("password_field")).sendKeys("test_data_920");
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest37();
    }
}
