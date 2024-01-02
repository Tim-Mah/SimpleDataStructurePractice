/* A Stack is a sequence of items which should be thought of as piled one on top of the 
 * other like a physical stack of boxes or cafeteria trays. 
 * 
 * Only the top item on the stack is accessible at any given time. 
 * 
 * Items are added to and reoveed from the top of the stack 
 * (LIFO - Last in, first out)
 * 
 * @Auther: Tim Mah
 * Date: Feb 25 2021
 */

public class Stack {
	Node top;
	private int size;
	
	/*
	 * An object of type Node holds one of the items
	 * in the linked list that represents the stack.
	 */
	private class Node
	{
		private Node link;
		private int info;

	}
	
	/**
	 * 	Checks if the stack is empty. 
	 * @return true if the stack is empty and false otherwise
	 */
	public boolean isEmpty()
	{
		if(top == null)
		{
			return true;
		}
		return false;
	}

	/**
	 * Add a new element (n) to the top of the Stack. 
	 * 
	 * @param n Integer to be added
	 */
	public void push(int n)
	{
		size++;
		Node temp = new Node();
		temp.info = n;
		temp.link = top;
		top = temp;

	}

	/**
	 * Remove the top item from the stack and return it.
	 * @return The top element
	 */
	public int pop()
	{
		if(top != null)
		{
		size--;
		}
		int info = top.info;
		top = top.link;
		return info;
	}	
	
	public int peek()
	{
		return top.info;
	}
	
	public int size()
	{
		return size;
	}

}
