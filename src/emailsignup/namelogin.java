package emailsignup;



import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;

public class namelogin {

	public static void main(String[] args) throws Exception 
	{
	 System.setProperty("webdriver.chrome.driver", "C:\\Users\\rajak\\Downloads\\chromedriver_win32\\chromedriver.exe\\");
	 ChromeOptions co = new ChromeOptions();
	 co.addArguments("--remote-allow-origins=*");
	 WebDriver driver = new ChromeDriver(co); 
	 driver.get("https://mail.google.com/");
	 driver.manage().window().maximize();
     driver.findElement(By.id("identifierId")).sendKeys("rajakaninagarajan4@gmail.com");
     ((WebElement) driver.findElements(By.xpath("//span[@class='VfPpkd vQzf8d']"))).click();
     driver.findElement(By.name("Passwd")).sendKeys("raji17200");
     driver.findElement(By.xpath("//span[@class='VfPpkd RLmnJb']")).click();
     Thread.sleep(2000);
		

	}

}
