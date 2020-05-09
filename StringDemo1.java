/*
This code builds a string
st is a reference, that is made from a class in Java called "String"
*/

class StringDemo1{
	public static void main(String[] args) {
		String st; //reference variable 
		int len_str;
		st = new String("Elementary, My dear Watson!"); 
		//the line above with "new" creates an object, and references to 
		//that object using st
		len_str = st.length();
		System.out.println("The length is: " + len_str);
	}
}