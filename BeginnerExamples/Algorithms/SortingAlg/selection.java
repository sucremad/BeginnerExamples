package algorithm;

public class selection {

	public void selection(int[] array) {

		for (int i = 0; i < array.length; i++) {



				for (int j = i + 1; j < array.length; j++) {
					if (array[j] < array[i]) {
						int temp=array[i];
						array[i]=array[j];
						array[j]=temp;
				}

			}
		}
	}
}
