import { Flex, FlexProps } from '../Flex/Flex';

type RowProps = Omit<FlexProps, 'direction'>

export const Row = (props: RowProps) => {
    return (
        <Flex direction='row' {...props} />
    );
};
