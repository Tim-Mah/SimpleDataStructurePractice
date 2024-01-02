/*
* @Auther: Tim Mah
* Date: Nov 10, 2020
*/
public class Nov10_SelectionSort {

	public static void main(String[] args) {

		int[] x = {8, 9, 6, 1, 2, 4};
		topSort(x, 2);
		for(byte b =0; b<x.length; b++)
		{
			System.out.print(x[b] + " ");
		}
	}
	public static void selectionSort(int[] x)
	{

		for(int i =x.length-1; i>=1; i--)
		{
			//find max value
			int indexMax = 0;
			for(byte b = 0; b<=i; b++)
			{
				if(x[b] > x[indexMax])//if the element at that index is bigger, change the max index
				{
					indexMax = b;
				}
			}
			//swap max value with end of the array

			//position of max is indexMax, postion want to swap is at i
			int temp = x[indexMax];
			x[indexMax] = x[i];
			x[i] = temp;
		}
	}
	public static void selectionSortSmall(int[] x)
	{
		//starts at 0, goes to length -1, bc that will already be sorted
		for(int i = 0; i < x.length-1; i++)
		{
			//checks every element to find the index of the smallest element.
			int mindex = x.length-1;
			for(int b = i; b< x.length; b++)//start it at i, because everything before i is sorted
			{
				if(x[mindex] > x[b])
				{
					mindex = b;
				}
			}
			//Switch the 2 values
			int temp = x[mindex];
			x[mindex] = x[i];
			x[i] = temp;
		}
	}
	public static void topSort(int a[], int k)
	{
		for(int i = a.length-1; i>= a.length-k; i--)
		{
			int maxindex = 0;
			for(int b = 0; b<= i; b++)
			{
				if(a[maxindex] < a[b])
				{
					maxindex = b;
				}
			}
			int temp = a[maxindex];
			a[maxindex] = a[i];
			a[i] = temp;
		}

	}
}
