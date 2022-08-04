// Method without recursion (slightly slower)
use std::time::Instant;

fn main() {
    let start = Instant::now();
    let mut sum_of_fit = 0;

    for degree in 1..11 {
        let mut series_list = Vec::new();
        for i in 1..degree+1 {
            series_list.push(ten_degree_polynomial(&i));
        }

        let dump = vec_of_vecs(&series_list);
        for diff_list in &dump {
            sum_of_fit += diff_list.last().expect("Error, no last element");
        };
        if dump.last().expect("Error").len() > 1 {
            let dump_last = dump.last().expect("Error, no last element");
            let dump_last_len = dump_last.len();
            sum_of_fit += dump_last[&dump_last_len-1] - dump_last[&dump_last_len-2];
        }
    }

    let duration = start.elapsed();
    println!("Sum of FITS: {}\nTime taken: {:?}", sum_of_fit, duration);
}

fn ten_degree_polynomial(n: &isize) -> isize {
    return 1 - n + n.pow(2) - n.pow(3) + n.pow(4) - n.pow(5) + n.pow(6) - n.pow(7) + n.pow(8) - n.pow(9) + n.pow(10);
}

fn difference_list(l: &Vec<isize>) -> Vec<isize> { 
    let mut different_list = Vec::new();

    for i in 1..l.len(){
        different_list.push(l[i] - l[i-1]);
    }
    return different_list
}

fn vec_of_vecs(list: &Vec<isize>) -> Vec<Vec<isize>> {
    let mut returnable_vect: Vec<Vec<isize>> = vec![list.to_vec()];
    for _ in (2..list.len()).rev() {
        returnable_vect.push(difference_list(&returnable_vect.last().expect("error getting last element")));
    }
    return returnable_vect
}

