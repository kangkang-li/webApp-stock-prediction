// written by: Jiawen.Sun Mingbo.Zhang
// assisted by: Jiawen.Sun Mingbo.Zhang
// debugged by: Jiawen.Sun Mingbo.Zhang
package servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import service.ILoginService;
import service.LoginServiceImpl;

public class LoginServlet extends HttpServlet{
	
	private ILoginService ls=new LoginServiceImpl();
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
			doPost(request,response);
	}

 
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		response.setContentType("text/html");  
		//��ǰ�˻�ȡ�˺�����
		String user=request.getParameter("user");
		 String pwd=request.getParameter("pwd");
		 //����DAO�����ݿ�
		 try {
			 boolean success =ls.login(user, pwd);
			 if(success){
				 response.sendRedirect("../stocks.jsp");
				  
				 //��¼�ɹ���ת��������
			 }
			 else{
				 //request.setAttribute("data", "xxxxxx");
				 //request.getRequestDispatcher("../stocks.jsp").forward(request, response);
				 response.getWriter().print("<script language='javascript'>alert('wrong user name or password!');window.location.href='../login.jsp'</script>");

			 }
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

	}

}
