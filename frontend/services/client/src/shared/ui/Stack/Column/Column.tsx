import { Flex, FlexProps } from '../Flex/Flex';

type ColumnProps = Omit<FlexProps, 'direction'>

export const Column = (props: ColumnProps) => {
    const { align = 'start' } = props;

    return (
        <Flex {...props} direction='column' align={align} />
    );
};
