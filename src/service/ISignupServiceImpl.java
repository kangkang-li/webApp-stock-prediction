// written by: Jiawen.Sun Mingbo.Zhang
// assisted by: Jiawen.Sun Mingbo.Zhang
// debugged by: Jiawen.Sun Mingbo.Zhang
package service;

import java.util.Map;

import dao.DbHelperImpl;

public class ISignupServiceImpl implements ISignupService {
	private DbHelperImpl dao=new DbHelperImpl();
	public boolean signup(String fname,String lname,String email,String pwd){
		String sql="select count(*) n from userinfo where email=?";
		Object[] params={email};
		Map row=dao.runSelect(sql, params)[0];
		int n=Integer.parseInt(row.get("n").toString());
		if(n==0){
			String ins="INSERT INTO userinfo (fname, lname,email,pwd) VALUES (?,?,?,?)";
			Object[] para={fname,lname,email,pwd};
			dao.runUpdate(ins, para);
			return true;
		}
		else return false;
	}
}
