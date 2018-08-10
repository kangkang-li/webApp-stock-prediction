// written by: KangKang.Li
// assisted by: Lang.Liu
// debugged by: Jiawen.Sun Mingbo.Zhang
package servlet;

import java.io.*;
import java.util.Iterator;
import java.util.Map;
import java.util.TreeMap;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import net.sf.json.JSONObject;
import service.IHistoryService;
import service.HistoryServiceImpl;
import service.IRealService;
import service.RealServiceImpl;
/**
 * Servlet implementation class Caller
 */

public class Caller extends HttpServlet {
	
	private static final long serialVersionUID = 1L;
	private IHistoryService hs=new HistoryServiceImpl();
	private IRealService rs=new RealServiceImpl();
	float[] callPY(String fileAddress,String stockSymbol, int isDailyInt) {
		
		float result[]= new float[12];
		fileAddress=fileAddress+"CallerPY.py";
		String command = "python " +fileAddress+" "+ stockSymbol;
		System.out.println(command);
        try {
        	Process process = Runtime.getRuntime().exec(command);
            InputStreamReader ir = new InputStreamReader(process.getInputStream());
            LineNumberReader input = new LineNumberReader(ir);
            for (int i=0;i<12;i++)
            	result[i] = Float.parseFloat(input.readLine());
            input.close();
            ir.close();
//            process.waitFor();
        } catch (IOException e) {
            // logger.error("reading error" + e.getMessage());
     	   System.out.println("error");
        }	
//		return Float.toString(result[0])+" "+Float.toString(result[1])+" "+Float.toString(result[2]);
		return result;
		}
	
	
    /**
     * @see HttpServlet#HttpServlet()
     */
    public Caller() {
        super();
        // TODO Auto-generated constructor stub
    }

    public static void readToBuffer(StringBuffer buffer, String filePath) throws IOException {
         InputStream is = new FileInputStream(filePath);
         String line; 
         BufferedReader reader = new BufferedReader(new InputStreamReader(is));
         line = reader.readLine(); 
         while (line != null) { 
             buffer.append(line); 
             buffer.append("\n"); 
  
             line = reader.readLine(); 
         }
         reader.close();
         is.close();
     }
	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		// String title="Prediction Algorithm\n";
		String optionStockSymbol = request.getParameter("optionStockSymbol");
		String json =hs.history(optionStockSymbol);
		String real=rs.getReal(optionStockSymbol);
		System.out.print(real);
		String base_path=request.getSession().getServletContext().getRealPath("");
		float[] resultPrediction=callPY(base_path,optionStockSymbol,1);
		
		String rnnPath=base_path+"\\rnn\\"+optionStockSymbol+"_rnn.json";
		
		 StringBuffer sb = new StringBuffer();
	        readToBuffer(sb, rnnPath);
	        JSONObject rnnjson=(JSONObject)JSONObject.fromObject(sb.toString()).get("Prediction");
	        Map m = rnnjson;
	        TreeMap mm=new TreeMap(m);
	        JSONObject rnnstr=JSONObject.fromObject(mm.get(mm.lastKey()));
	        String rnn_close=rnnstr.get("4. close").toString();
	        String rnn_open=rnnstr.get("1. open").toString();
	        String rnn_high=rnnstr.get("2. high").toString();
	        String rnn_low=rnnstr.get("3. low").toString();

	          
          
        String resultJsonStr="{'predictedPrice':{"+"'open':'"+resultPrediction[0]+"',"+
        									    "'high': '"+resultPrediction[1]+"',"+
        									    "'low':'"+resultPrediction[2]+"',"+
        									    "'close':'"+resultPrediction[3]+"'"+
        									"},"+
        					"'historicalAccuracy': '"+resultPrediction[4]+"',"+
        					"'fluctuationRange': '"+resultPrediction[5]+"'}";
        
        
//        for(float f : resultPrediction)
//        	System.out.println(f);
        
        
        JSONObject jsonobj = JSONObject.fromObject(json);
        Iterator<?> keys = jsonobj.keys();
        String key = null;
        
        float highest_close = 0;
        float lowest_close = Float.MAX_VALUE;
        
        while( keys.hasNext() ) {
            key = (String)keys.next();
            float tmp = Float.parseFloat((String) ((JSONObject) jsonobj.get(key)).get("close"));
            if (tmp > highest_close) {
            	highest_close = tmp;
            }
            if (tmp < lowest_close) {
            	lowest_close = tmp;
            }
        }
        
        request.getSession().setAttribute("highest_close", Float.toString(highest_close));
        request.getSession().setAttribute("lowest_close", Float.toString(lowest_close));
        
        float latest_close = Float.parseFloat((String) ((JSONObject) jsonobj.get(key)).get("close"));
        int count = 0;
        
        if (latest_close < resultPrediction[3]) {
        	count++;
        }
        if (latest_close < resultPrediction[9]) {
        	count ++;
        }
        if (latest_close < Float.parseFloat(rnn_close)) {
        	count ++;
        }
        
        if (count >= 2) {
        	request.getSession().setAttribute("recommendation", "Buy");
        }
        else {
        	request.getSession().setAttribute("recommendation", "Sale");
        }
        
        JSONObject jj= JSONObject.fromObject(real);
		request.getSession().setAttribute("data", json);
		request.getSession().setAttribute("stocksymbol", optionStockSymbol);
		
		request.getSession().setAttribute("bayesian_close", Float.toString(resultPrediction[3]));
		request.getSession().setAttribute("bayesian_high", Float.toString(resultPrediction[1]));
		request.getSession().setAttribute("bayesian_low", Float.toString(resultPrediction[2]));
		request.getSession().setAttribute("bayesian_open", Float.toString(resultPrediction[0]));
		request.getSession().setAttribute("bayesian_acc", Float.toString(resultPrediction[4]));
		request.getSession().setAttribute("bayesian_rng", Float.toString(resultPrediction[5]));
		
		
		request.getSession().setAttribute("ann_close", Float.toString(resultPrediction[9]));
		request.getSession().setAttribute("ann_open", Float.toString(resultPrediction[6]));
		request.getSession().setAttribute("ann_high", Float.toString(resultPrediction[7]));
		request.getSession().setAttribute("ann_low", Float.toString(resultPrediction[8]));
		request.getSession().setAttribute("ann_acc", Float.toString(resultPrediction[10]));
		request.getSession().setAttribute("ann_rng", Float.toString(resultPrediction[11]));
		
		
		request.getSession().setAttribute("lstm_close", rnn_close);
		request.getSession().setAttribute("lstm_open", rnn_open);
		request.getSession().setAttribute("lstm_high", rnn_high);
		request.getSession().setAttribute("lstm_low", rnn_low);

		
		
		request.getSession().setAttribute("real_time", (String)jj.get("time"));
		request.getSession().setAttribute("real_high", (String)jj.get("high"));
		request.getSession().setAttribute("real_low", (String)jj.get("low"));
		request.getSession().setAttribute("real_close", (String)jj.get("close"));
		request.getSession().setAttribute("real_open", (String)jj.get("open"));
		request.getSession().setAttribute("real_volume", (String)jj.get("volume"));
		response.sendRedirect("../stocks.jsp"+"#"+optionStockSymbol);
		
		

	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}
	
	
}
