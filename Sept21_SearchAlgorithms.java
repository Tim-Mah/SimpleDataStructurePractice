/*
* @auther: Tim Mah
* Date: Sept. 21 2020
*/
public class Sept21_SearchAlgorithms 
{

	public static void main(String[] args) 
	{
		/*
		 * Algorithms are series of step by step instructions for solving a problem.
		 * 
		 * 1. Linear Search
		 * Check every position in the array, one at a time and 
		 * return the index for the element we are looking for, or -1 if it's not there.
		 * pros: easy to use
		 * quick for small arrays
		 * always correct
		 * 
		 * cons: heavy on process power or time
		 */
		
		/*
		 * 2. Binary search (must be sorted)
		 * 
		 * Look at the number in the middle
		 * is it above or below that value. 
		 * Then find the middle value of the upper/lower half, and keep repeating
		 */
		int[] b = {2, 4, 5, 7, 9, 10, 12, 14, 17, 20, 21};
		int[] c = {100, 98, 87, 76, 62, 59, 58, 46, 45, 39, 34, 21, 10};
		int[] hw = {23, 27, 30, 34, 41, 49, 51, 55, 57, 60, 67, 72, 78, 83, 96};
		System.out.println(binarySearch(b, 18));
		/*for #2
		 * min= 0, max = 10, middle = 5
		 * min=0, max = 4, middle = 2;
		 * min=0, max = 1, middle =0
		 * min=0, max =0; middle=0;
		 * 
		 * #18
		 * 0,10,5
		 * 6,10,8
		 * 9,10,9
		 * 9,8 - impossible, so not in list
		 */
		
	}
	public static int linearSearch(int[] a, int b)
	{
		for(int i=0; i< a.length; i++)
		{
			if(a[i] ==b)
			{
				return i;
			}
		}
		return -1;
	}
	public static int binarySearch(int[] a, int b)
	{
		int min =0;
		int max = a.length-1;
		int middle = (min+max)/2;
		while(max>=min)
		{
			System.out.println(min + "," + max + "," + middle);
			if(a[middle] ==b)
			{
				return middle;
			}else if(b>a[middle])
			{
				min = middle+1;
				middle = (min+max)/2;
			}else//b is less than
			{
				max =middle-1;
				middle = (min+max)/2;
			}
		}
		return -1;//element isn't in the list
	}
	public static int binarySearchRev(int[] a, int b)
	{
		int[] c = {100, 98, 87, 76, 62, 59, 58, 46, 45, 39, 34, 21, 10};
		int Max = 0;
		int Min = a.length-1;
		int middle = (Max+Min)/2;
		while(Min>=Max)
		{
			System.out.println(Max + "," + Min + "," + middle);
			if(a[middle] ==b)
			{
				return middle;
			}else if(b>a[middle])
			{
				Min = middle-1;
				middle = (Max+Min)/2;
			}else//b is less than
			{
				Max =middle+1;
				middle = (Max+Min)/2;
			}
		}
		return -1;//element isn't in the list
	}
}
