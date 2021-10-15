// Java Program to convert
// Set to List in Java 8

import java.util.*;
import java.util.stream.*;

class STL {

	// Generic function to convert set to list
	public static <T> List<T> convertSetToList(Set<T> set)
	{
		// create a list from Set
		List<T> list = new ArrayList<>(set);

		// return the list
		return list;
	}

	public static void main(String args[])
	{

		// Create a Set using HashSet
		Set<String> hash_Set = new HashSet<String>();

		// Add elements to set
		hash_Set.add("Apple");
		hash_Set.add("Ball");
		hash_Set.add("Cat");
		hash_Set.add("Doll");
		hash_Set.add("Eagle");

		// Print the Set
		System.out.println("Set: " + hash_Set);

		// construct a new List from Set
		List<String> list = convertSetToList(hash_Set);

		// Print the List
		System.out.println("List: " + list);
	}
}
