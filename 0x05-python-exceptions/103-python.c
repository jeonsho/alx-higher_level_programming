#include <Python.h>

/**
 *print_python_list - Prints information about a Python list.
 *@p: A pointer to a Python object representing a list.
 *
 *Description:
 *This function prints details about a Python list, including its size,
 *allocated memory, and information about each element within the list.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size;
	PyObject * item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[*] Python list info\n [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n[*] Size of the Python List
		       	= %ld\n[*] Allocated = %ld\n", size, ((PyListObject*) p)->allocated);
	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 *print_python_bytes - Prints information about a Python bytes object.
 *@p: A pointer to a Python object representing bytes.
 *
 *Description:
 *This function prints details about a Python bytes object, including its
 *size, string representation, and the first 10 bytes in hexadecimal format.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[.] bytes object info\n [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("[.] bytes object info\n  size: %ld\n  trying string:
		       	%s\n  first 10 bytes: ", size, str);
	for (i = 0; i < size && i < 10; i++)
	{
		printf("%02x", (unsigned char) str[i]);
		if (i < size - 1)
			printf(" ");
	}

	printf("\n");
}

/**
 *print_python_float - Prints information about a Python float object.
 *@p: A pointer to a Python object representing a float.
 *Description:
 *This function prints details about a Python float object, including its value
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[.] float object info\n [ERROR] Invalid Float Object\n");
		return;
	}

	printf("[.] float object info\n  value: %f\n", PyFloat_AsDouble(p));
}
