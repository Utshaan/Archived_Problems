use std::time::Instant;

fn main() {
    let start = Instant::now();
    let mut sum_of_fit = 0;

    for degree in 1..11 {
        let mut series_list = vec![0;degree];
        let mut nth_term : i64 = 1;
        for i in 1..degree+1 {
            series_list[i-1] = ten_degree_polynomial(&nth_term);
            nth_term = nth_term + 1;
        }

        let ans = next_term(&series_list);
        sum_of_fit = sum_of_fit + ans;
    }

    let duration = start.elapsed();
    println!("{sum_of_fit}");
    println!("Time taken = {:?}", duration)


}

fn ten_degree_polynomial(n: &i64) -> i64 {
    return 1 - n + n.pow(2) - n.pow(3) + n.pow(4) - n.pow(5) + n.pow(6) - n.pow(7) + n.pow(8) - n.pow(9) + n.pow(10);
}

fn next_term(l: &[i64] ) -> i64 {
    if l.len() == 1 {
        return l[l.len() -1]
    } else {
        return l[l.len() -1] + next_term(&difference_list(l));
    }
}

fn difference_list(l: &[i64]) -> Vec<i64> { 
    let mut different_list = vec![0;l.len() -1];

    for i in 1..l.len(){
       different_list[i-1] = l[i] - l[i-1];
    }
    return different_list
}

/* Method without recursion (slightly slower)
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
*/