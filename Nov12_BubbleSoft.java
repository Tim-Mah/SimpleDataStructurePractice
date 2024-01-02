/*
* @Auther: Tim Mah
* Date: Nov 12, 2020
*/
public class Nov12_BubbleSoft {

	public static void main(String[] args) {
		String[] list = {"a", "a", "a", "b"};
		//shakerSort(list);
		bubbleSort(list);
		for(int i =0; i< list.length; i++)
		{
			System.out.println(list[i] + " ");
		}
	}
	public static void bubbleSort(String[] list)
	{
		boolean isSorted = false;
		while(isSorted == false)
		{
			isSorted = true;
			for(byte b = 0; b<list.length-1; b++)//Can't do the last one because there isn't another one after that to compare it too
			{
				if(list[b].compareToIgnoreCase(list[b+1]) < 0)// if the result is greater than 0, it means that list[b] is greater than list[b+1]
				{
					isSorted = false;
					String temp = list[b+1];
					list[b+1] = list[b];
					list[b] = temp;
				}//end if
			}//end for
		}//end while
	}//end bubbleSort

	public void actualBubbleSort(String[] list)
	{
		boolean isSorted = false;
		while(!isSorted) //isSorted == false
		{
			isSorted = true;
			for(int i = 0; i < list.length-1; i++) {
				//stop at the second last index.
				if(list[i].compareToIgnoreCase(list[i+1]) > 0)
				{
					isSorted = false; //list was not sorted
					String temp = list[i];
					list[i] = list[i+1];
					list[i+1] = temp;
				}

			}

		}
	}

	public static void shakerSort(String[] list)
	{
		boolean isSorted = false;
		//while loop to run until it is sorted
		while(isSorted == false)
		{
			//for loop for ascending
			for(byte b = 0; b<list.length-1; b++)
			{
				isSorted = true;
				//if the if statement runs, it is not sorted
				if(list[b].compareToIgnoreCase(list[b+1]) > 0)
				{
					isSorted = false;
					String temp = list[b];
					list[b] = list[b+1];
					list[b+1] = temp;
				}
				for(int i =0; i< list.length; i++)
				{
					System.out.print(list[i] + " ");
				}
				System.out.println();
			}
			//for loop for descending
			for(byte c = (byte) (list.length-2); c>0; c--)
			{
				isSorted = true;
				if(list[c-1].compareToIgnoreCase(list[c]) > 0)
				{
					isSorted = false;
					String temp = list[c];
					list[c] = list[c-1];
					list[c-1] = temp;
				}
				for(int i =0; i< list.length; i++)
				{
					System.out.print(list[i] + " ");
				}
				System.out.println();
			}

		}//end while
	}
}

