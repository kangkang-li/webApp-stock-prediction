package dao;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.Map;
import javax.servlet.jsp.jstl.sql.Result;
import javax.servlet.jsp.jstl.sql.ResultSupport;
/**
 * @author Jiawen Sun
 */
public  class DbHelperImpl implements IDbhelper {
	private final String DRIVER="com.mysql.jdbc.Driver";
	//private final String DRIVER="oracle.jdbc.driver.OracleDriver";
	private final String URL="jdbc:mysql://localhost:3306/stock?useUnicode=true&characterEncoding=utf-8&useSSL=false";
	//private final String URL="jdbc:oracle:thin:@localhost:1521:XE";
	

	private Connection getConnection(){		
		try{

			//Class.forName("com.mysql.cj.jdbc.Driver");
			Class.forName(DRIVER);
			Connection conn=DriverManager.getConnection(URL, "root", "sjw441500");
			return conn;
		}catch (Exception e) {
			e.printStackTrace();
			return null;
		}
	}	
	

	public Map[] runSelect(String sql,Object[] params){
		Connection conn=null;
		PreparedStatement ps=null;
		ResultSet rs=null;
		try{			
			conn=getConnection();
			ps=conn.prepareStatement(sql);
		
			for(int i=0;i<params.length;i++){
				ps.setObject(i+1, params[i]);
			}					 	
			rs=ps.executeQuery();
			Result result=ResultSupport.toResult(rs);
			Map[] rows=result.getRows();			
			return rows;
		}catch (Exception e) {
			e.printStackTrace();
			return null;
		}finally{ 
			try{
				rs.close();
				ps.close();				
				conn.close();
			}catch (Exception e) {
				e.printStackTrace();
			}
		}				
	}
			

	public Map[] runSelect(String sql){
		Connection conn=null;
		PreparedStatement ps=null;
		ResultSet rs=null;
		try{			
			conn=getConnection();
			ps=conn.prepareStatement(sql);
			rs=ps.executeQuery();
			Result result=ResultSupport.toResult(rs);
			Map[] rows=result.getRows();			
			return rows;
		}catch (Exception e) {
			e.printStackTrace();
			return null;
		}finally{ 
			try{
				rs.close();
				ps.close();				
				conn.close();
			}catch (Exception e) {
				e.printStackTrace();
			}
		}				
	}
	

	public void runUpdate(String sql){
		Connection conn=null;
		PreparedStatement ps=null;
		try{			
			conn=getConnection();
			ps=conn.prepareStatement(sql);
		
			ps.executeUpdate();
		}catch (Exception e) {
			e.printStackTrace();
		}finally{
			try{
				ps.close();				
				conn.close();
			}catch (Exception e) {
				e.printStackTrace();
			}
		}				
	}
	

	public void runUpdate(String sql,Object[] params){
		Connection conn=null;
		PreparedStatement ps=null;
		try{			
			conn=getConnection();
			ps=conn.prepareStatement(sql);
	
			for(int i=0;i<params.length;i++){
				ps.setObject(i+1, params[i]);
			}	
			ps.executeUpdate();
		}catch (Exception e) {
			e.printStackTrace();
		}finally{ 
			try{
				ps.close();				
				conn.close();
			}catch (Exception e) {
				e.printStackTrace();
			}
		}				
	}
		


}
