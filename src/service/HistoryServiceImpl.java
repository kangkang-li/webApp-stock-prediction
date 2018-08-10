// written by: Jiawen.Sun Mingbo.Zhang
// assisted by: Jiawen.Sun Mingbo.Zhang
// debugged by: Jiawen.Sun Mingbo.Zhang

package service;

import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

import dao.DbHelperImpl;
import net.sf.json.JSONObject;

public class HistoryServiceImpl implements IHistoryService {
	private DbHelperImpl dao=new DbHelperImpl();
	
	public String history(String name){
		String sql="select open,date,high,low,close,volume from historical_stock where symbol=? order by date";
		Object[] params={name};
		Map[] row=dao.runSelect(sql, params);
		Map ans =new TreeMap();
		for(Map m:row ){
			Map tmp =new HashMap();
			tmp.put("open",  m.get("open"));
			tmp.put("close",  m.get("close"));
			tmp.put("high", m.get("high"));
			tmp.put("low",  m.get("low"));
			tmp.put("volume",  m.get("volume"));

			ans.put(m.get("date").toString(), tmp);
			
		}
		
		JSONObject json = JSONObject.fromObject(ans);
		return json.toString();
	}
	

}
