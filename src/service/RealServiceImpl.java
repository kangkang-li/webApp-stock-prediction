// written by: Jiawen.Sun Mingbo.Zhang
// assisted by: Jiawen.Sun Mingbo.Zhang
// debugged by: Jiawen.Sun Mingbo.Zhang
package service;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.*;

import org.apache.commons.compress.utils.IOUtils;

import net.sf.json.JSONArray;
import net.sf.json.JSONObject;

public class RealServiceImpl implements IRealService {

	@Override
	public String getReal(String name) {
		// TODO Auto-generated method stub
		String head ="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+name+"&interval=1min&outputsize=compact&apikey=IV7A1W1XH6CO5W4X";
		try{
		URL url = new URL(head);
		System.out.println("URL:"+head);
		URLConnection conn = url.openConnection();
		String body =readResponseBody(conn.getInputStream());
		
		JSONObject json = JSONObject.fromObject(body);
		JSONObject data1 =(JSONObject)json.get("Meta Data");
		String time=(String)data1.get("3. Last Refreshed");
		JSONObject data2=(JSONObject)json.get("Time Series (1min)");
		JSONObject dataItem=(JSONObject) data2.get(time);
		String open = dataItem.getString("1. open");
		String high = dataItem.getString("2. high");
		String  low= dataItem.getString("3. low");
		String close = dataItem.getString("4. close");
		String volume = dataItem.getString("5. volume");
		JSONObject j= new JSONObject();
		j.element("time", time);
		j.element("open", open);
		j.element("high", high);
		j.element("low", low);
		j.element("close", close);
		j.element("volume", volume);
		
		return j.toString();
		
		}
		catch(Exception e){
			e.printStackTrace();
		}
		return "";

	}
	
	private String readResponseBody(InputStream inputStream) throws IOException {
		 
	    BufferedReader in = new BufferedReader(
	            new InputStreamReader(inputStream));
	    String inputLine;
	    StringBuffer response = new StringBuffer();
	 
	    while ((inputLine = in.readLine()) != null) {
	        response.append(inputLine);
	    }
	    in.close();
	     
	    return response.toString();
	}

}
