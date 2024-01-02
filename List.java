
public class List
{
	private Node head; 

	// inner class, visible only to the List class 
	class Node { 
		int info; // can be changed to anything we want 
		Node link; // reference to next node in list 

		// constructor method 
		Node (int i, Node n) { 
			info = i; 
			link = n;
		} 
	} //end Node class
	public void addAtFront(int n)
	{
		Node node = new Node(n, head);

		head = node;
	}
	public void printList()
	{
		Node temp = head;
		String a = "[";
		try
		{
			while(temp != null){
				a += temp.info + ", ";
				temp = temp.link;
			}
			a = a.substring(0, a.length()-2);
			a += "]\n";
			System.out.println(a);

		}catch(StringIndexOutOfBoundsException e)
		{
			System.out.println("Your list is empty.");
		}
	}
	public void printList2()
	{
		Node temp = head;
		String a = "[";
		if(temp == null)
		{
			System.out.println("Your list is empty.");
		}else
		{
			while(temp != null)
			{
				a += temp.info + ", ";
				temp = temp.link;
			}
			a = a.substring(0, a.length()-2);
			a += "]";
			System.out.println(a);
		}
	}
	public int sum()
	{
		Node temp = head;
		int a = 0;
		if(temp ==null)
		{
			return 0;
		}else
		{
			while(temp !=null){
				a += temp.info;
				temp = temp.link;
			}
			return a;
		}
	}

	public void deleteFirst()
	{
		if(head != null)
		{
			head = head.link;
		}
	}

	/*public void deleteLast()
	{
		if(head != null)
		{
			Node temp = head;
			//Node temp2 = head;
			if(temp.link == null)
			{
				head = temp.link;
			}else
			{
				while(temp.link.hasNext())
				{
					temp = temp.link;
					//temp2 = temp2.link;
				}
				temp.link = temp.link.link;
			}
		}
	}*/
	public void deleteLast()
	{
		if(head != null)
		{
			Node temp = head;
			//Node temp2 = head;
			if(temp.link == null)
			{
				head = null;//or could make head == null, bc it's the same thing.
			}else
			{
				while(temp.link.link !=null)
				{
					temp = temp.link;
					//temp2 = temp2.link;
				}
				temp.link = null;//or set it equal to null, bc i didn't know I could do that.
			}
		}
	}

	public int countNodes()
	{
		Node temp = head;

		if(temp == null)
		{
			return 0;
		}else
		{
			int count = 0;
			while(temp != null)
			{
				count++;
				temp = temp.link;
			}
			return count;
		}
	}

	public void addAtEnd(int v)
	{
		if(head == null)//no nodes
		{
			Node node = new Node(v, null);
			head = node;
		}else//anything else
		{
			Node temp = head;
			while(temp.link != null)
			{
				temp = temp.link;
			}//now temp is null
			temp.link = new Node(v, null);
		}
	}

	public void insert(int v, int n)
	{
		if(n<this.countNodes() && n>=0)
		{
			if(head!=null && this.countNodes() >= n)
			{
				if(n == 0)
				{
					this.addAtFront(v);
				}else
				{
					Node temp = head;
					int count = -1;
					while(count < n-2)
					{
						count++;
						temp = temp.link;
					}
					Node node = temp.link;
					temp.link = new Node(v, node);	
				}
			}
		}
	}

	public void delete(int n)
	{
		if(n<this.countNodes() && n>=0)
		{
			if(n ==0)
			{
				head = head.link;
			}else
			{
				Node temp = head;
				int count = -1;
				while(count < n-2)
				{
					count++;
					temp = temp.link;
				}
				temp.link = temp.link.link;	
			}
		}
	}

	public boolean contains(int i)
	{
		Node temp = head;
		while(temp != null)
		{
			if(temp.info == i)
			{
				return true;
			}
			temp = temp.link;
		}
		return false;
	}

	public void deleteAll(int i)
	{
		Node temp = head;
		while(temp.info == i)//at the start
		{
			head = temp.link;
			temp = head;
		}
		int counter = 2;
		while(temp.link != null && counter < this.countNodes())
		{
			if(temp.link.info == i)
			{
				temp.link = temp.link.link;
			}
			temp = temp.link;
			counter ++;
		}
		if(temp.link != null && counter == this.countNodes() && i == temp.link.info)//at the beginning
		{
			temp.link = null;
		}
	}

	public boolean isOrderedIncreasing()
	{
		Node temp = head;
		while(temp.link != null)
		{
			if(temp.info > temp.link.info)
			{
				return false;
			}
			temp = temp.link;
		}
		return true;
	}

	public boolean isIdentical(List l)
	{
		if(l.countNodes() == this.countNodes())//same length
		{
			Node temp = head;
			Node templ = l.head;
			while(temp != null && templ != null)
			{
				if(temp.info != templ.info)
				{
					return false;
				}
				temp = temp.link;
				templ = templ.link;
			}
		}
		return true;
	}
}
