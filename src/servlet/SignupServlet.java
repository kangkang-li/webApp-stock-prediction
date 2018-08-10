// written by: Jiawen.Sun Mingbo.Zhang
// assisted by: Jiawen.Sun Mingbo.Zhang
// debugged by: Jiawen.Sun Mingbo.Zhang
package servlet;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


import service.ISignupService;
import service.ISignupServiceImpl;
public class SignupServlet extends HttpServlet {

	private ISignupService ls=new ISignupServiceImpl();
	public void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
			doPost(request,response);
	}

 
	public void doPost(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		response.setContentType("text/html");  
		//从前端获取账号密码
		String email=request.getParameter("email");
		 String pwd=request.getParameter("pwd");
		 String fname=request.getParameter("fname");
		 String lname=request.getParameter("lname");
		 //连接DAO层数据库
		 try {
			 boolean success =ls.signup(fname, lname, email, pwd);
			 //boolean success = true;
			 if(success){
				 response.sendRedirect("../login.jsp");
				 //注册成功成功跳转到主界面
			 }
			 else{
				 response.getWriter().print("<script language='javascript'>alert('signup failed!');window.location.href='../register.jsp'</script>");
				 //注册失败跳转到错误界面
			 }
			} catch (Exception e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}

	}
}
