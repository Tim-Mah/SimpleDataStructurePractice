import java.util.*;
public class Nov11_InsertionSort {

	public static void main(String[] args) {
		int[] x = {8, 9, 6, 1, 4, 4};
		/*insertionSort(x);
		for(byte b =0; b<x.length; b++)
		{
			System.out.print(x[b] + " ");
			
		} */
		median();
		planets();
	}
	public static void insertionSort(int a[])
	{
		//starts at index 1, then goes through all of them
		//meaning if it is a length of 5, {0, 1, 2, 3, 4, 5}
		//for-loop would run 5 times

		for(byte b = 1; b<a.length; b++)
		{
			//compare 1 before, if it is bigger, slide it 1 to the right (before, save a[b])
			//compare 2 before, if it is bigger, slide it 1 to the right, etc.
			int temp = a[b];
			int i=1;
			while((b-i)>=0 && a[b-i]>temp)
			{
				a[b-i+1] = a[b-i];
				i++;
			}
			a[b-i+1] = temp;
		}
	}

	public static void correctInsertion(int list[])
	{
		for(int index = 1; index < list.length; index++)
		{
			int item = list[index]; // temporary storage of item
			int i = index;
			while (i > 0 && item < list[i-1])
			{
				// shift larger items to the right by one
				list[i] = list[i-1];
				// prepare to check the next item to the left
				i--;
			}
			list[i] = item; // put sorted item in open location
		}
	}
	
	public static void planets()
	{
		/*
		 * Write a program that initializes an array with the names of the planets 
		 * in their typical order (from closest to furthest from the Sun) 
		 * and prints them in that order on one line. 
		 * 
		 * The program should then use an insertion sort algorithm to arrange the names alphabetically. 
		 * To trace the progress of the sort, have it print the list after each pass.
		 */
		String[] planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"};
		for(byte b = 0; b< planets.length; b++)
		{
			System.out.print(planets[b] + " ");
		}
		System.out.println();
		
		//insertion Sort
		
		for(byte b = 1; b<planets.length; b++)//goes through every element
		{
			byte index = b;
			String temp = planets[b];
			
			while(index > 0 && planets[index-1].compareTo(temp) > 0)
			{
				planets[index] = planets[index-1];
				index--;
			}
			planets[index] = temp;
		}
		for(byte b =0; b<planets.length; b++)
		{
			System.out.print(planets[b] + " ");
		}
	}
	public static void median()
	{
		/* Write a program that prompts the user for the number of items to be processed,
		 * reads that many real values, and then finds their median. 
		 */
		Scanner sn = new Scanner(System.in);
		System.out.println("How many numbers do you want to input?");
		int[] a = new int[sn.nextInt()];
		for(byte b = 0; b< a.length; b++)
		{
			System.out.println("Input a value");
			a[b] = sn.nextInt();
		}
		
		//sort it using insertion sort
		for(byte b = 1; b<a.length; b++)
		{
			int temp = a[b];
			int index = b;
			while(index>0 && a[index-1] > temp)
			{
				a[index] = a[index-1];//shirting it up
				index--;
			}
			a[index] = temp;
		}
		//if a.length%2 is 1, it is odd, so select the middle one
		int median = 0;
		if(a.length%2 == 1)
		{
			median = a[a.length/2];
			System.out.println("if ran");
		}else
		{
			median = (a[a.length/2] + a[a.length/2 -1])/2;
			System.out.println("else ran");
		}
		System.out.println(median);
		//else take the middle 2 and avg them
	}

}
