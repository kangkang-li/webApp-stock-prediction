// written by: Jiawen.Sun Mingbo.Zhang
// assisted by: Jiawen.Sun Mingbo.Zhang
// debugged by: Jiawen.Sun Mingbo.Zhang
package service;
import java.util.Map;

import dao.DbHelperImpl;
public class LoginServiceImpl implements ILoginService {
	
	private DbHelperImpl dao=new DbHelperImpl();
	public boolean login(String para1,String para2){
		String sql="select count(*) n from userinfo where email=? and pwd=?";
		Object[] params={para1,para2};
		Map row=dao.runSelect(sql, params)[0];
		int n=Integer.parseInt(row.get("n").toString());
		return n==1;
	}

}
