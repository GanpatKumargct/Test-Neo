package testscenario;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import java.time.Duration;

public class TestScenario3 {
    public static void executeTest3() {
        /*
         * Dummy test run for scenario 3
         */
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
        driver.get("https://dummy.example.com/page_3");

        try {
            driver.findElement(By.id("user_name")).sendKeys("test_data_432");
            driver.findElement(By.id("checkout_btn")).sendKeys("test_data_855");
            driver.findElement(By.linkText("Log Out")).click();
            driver.findElement(By.className("nav-item")).sendKeys("test_data_526");
            driver.findElement(By.className("nav-item")).sendKeys("test_data_763");
            Thread.sleep(2000);
            driver.findElement(By.name("password_field")).sendKeys("test_data_566");
            driver.findElement(By.id("checkout_btn")).click();
            driver.findElement(By.id("user_name")).click();
            driver.findElement(By.linkText("Log Out")).sendKeys("test_data_159");
            if (!driver.getTitle().contains("Dashboard")) {
                System.out.println("Dashboard not in title");
            }
            driver.findElement(By.id("user_name")).sendKeys("test_data_172");
            Thread.sleep(2000);
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            driver.quit();
        }
    }
    
    public static void main(String[] args) {
        executeTest3();
    }
}
