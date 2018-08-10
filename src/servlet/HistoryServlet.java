// written by: Jiawen.Sun Mingbo.Zhang
// assisted by: Jiawen.Sun Mingbo.Zhang
// debugged by: Jiawen.Sun Mingbo.Zhang
package servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import net.sf.json.JSONObject;
import service.IHistoryService;
import service.HistoryServiceImpl;

public class HistoryServlet extends HttpServlet{
	
	private IHistoryService hs=new HistoryServiceImpl();
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
			doPost(request,response);
	}

 
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		response.setContentType("text/html");  

		String symbol=request.getParameter("optionStockSymbol");

	
		 try {
			 String json =hs.history(symbol);
			 if(!json.isEmpty()){
				 request.getSession().setAttribute("data", json);
				 response.sendRedirect("../stocks.jsp"+"#"+symbol);
				
			 }
			 else{

			 }
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

	}

}
