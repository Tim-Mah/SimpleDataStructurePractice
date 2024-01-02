/* A Queue is a sequence of items. It has 2 ends, the
 * front and the back. 
 * 
 * Items are added to the back of the queue and 
 * removed from the front. (FIFO - Fisrt in, first out)
 *  
 * @Auther: Tim Mah
 * Date: Feb 25 2021
 */

public class Queue {


	/**
	 * An object of type Node holds one of the items
	 * in the linked list that represents the queue.
	 */
	private class Node
	{
		private String info;
		private Node link;
		//Add private attribute(s)
	}


	//Add private attribute(s) for the Queue class.
	//What does a Queue reference? 
	private Node front;
	private Node back;
	private int size;

	/**
	 * Checks if the queue is empty. 
	 * @return  true if the queue is empty.
	 */
	boolean isEmpty() {
		if(front == null && back == null)
			return true;
		else
			return false;
	}


	/**
	 * Add N to the back of the queue.
	 * @param N String to be added to the queue
	 */
	public void add(String N ) {
			//set front and back to same node
			Node newNode = new Node();
			newNode.info = N;
			size++;
			if(isEmpty()) {
				//set front and back to the same node
				front = newNode;
				back = newNode;
			}else
			{
				back.link = newNode;
				back = newNode;
			}
			
	}

	/**
	 * Remove and return the front item in the queue.
	 * returns null if the queue is empty.
	 * @return the String at the front of the queue
	 */ 

	public String remove() {
		String temp;
		if(front !=null)
		{
			size--;
			 temp = front.info;
		front =front.link;
		return temp;
		}
		return null;
	}
	
	public int size()
	{
		return size;
	}
	
	public static void main(String[] args)
	{
		Queue q = new Queue();
		System.out.println(q.isEmpty());
		q.add("Alex");
		q.add("Tim");
		q.add("Luke");
		q.add("Jacob");
		q.add("Ben");
		q.add("Trevor");
		System.out.println(q.remove());
		System.out.println(q.remove());
		System.out.println(q.size());
	
	}


} // end class QueueOfInts
